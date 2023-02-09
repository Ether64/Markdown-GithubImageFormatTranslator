import { Plugin, TFile } from "obsidian";

const CDN = "https://cdn.ethereal.bond/file/github-images/";

export default class DopePlugin extends Plugin {
	reload() {
		const id: string = this.manifest.id,
			plugins = this.app.plugins;
		plugins.disablePlugin(id).then(() => plugins.enablePlugin(id));
	}

	async onload() {
		await this.loadSettings();

		const _ribbon = this.addRibbonIcon(
			"checkmark",
			"Convert to Github Images",
			async (evt: MouseEvent) => {
				const currentFile =
					this.app.workspace.getActiveFile() ?? new TFile();

				const contents = await this.app.vault.read(currentFile);
				const converted = contents.replace(
					/\!\[\[(.*)\]\]/g,
					(_match, imgPath, _) => {
						const link = encodeURIComponent(imgPath).replace(
							/%20/g,
							"+"
						);
						return `![](${CDN}${link})`;
					}
				);

				const newFilePath = currentFile.path.replace(".md", ".gh.md");
				let newFile = this.app.vault.getAbstractFileByPath(newFilePath);

				if (newFile === null)
					newFile = await this.app.vault.create(newFilePath, "");

				this.app.vault.modify(newFile, converted);

				// this.reload()
			}
		);

		this.addCommand({
			id: "reloadGhFormatter",
			name: "Reload GitHub Formatter (dev)",
			callback: () => {
				this.reload();
			},
		});

		// If the plugin hooks up any global DOM events (on parts of the app that doesn't belong to this plugin)
		// Using this function will automatically remove the event listener when this plugin is disabled.
		this.registerDomEvent(document, "click", (evt: MouseEvent) => {
			// console.log('click', evt);
		});

		// When registering intervals, this function will automatically clear the interval when the plugin is disabled.
		this.registerInterval(
			window.setInterval(() => console.log("setInterval"), 5 * 60 * 1000)
		);
	}

	onunload() {}

	async loadSettings() {
		// this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
	}

	async saveSettings() {
		// await this.saveData(this.settings);
	}
}
